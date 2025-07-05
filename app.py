import streamlit as st
from src.search import response
from src.companylist import com_list
from src.save import save

def main():

    try : 
        st.set_page_config("Find HR Profile")
        st.title("Find HR Profile ...")
        file = st.file_uploader(
                "Upload your file", 
                type=["xlsx"],  
                accept_multiple_files=False
            )
        st.info("Make sure it has company column")
        if st.button("submit & process"):
                with st.spinner("Fetching..."):
                    if file:
                        company_list=com_list(file)
                        results=[]

                        for company in company_list:
                            st.write(f"fetching contacts for {company} ...")
                            res=response(company)

                            for result in res.get('organic', []):
                                title = result.get('title', '').lower()
                                snippet = result.get('snippet', '').lower()
                                link = result.get('link')

                                # Check if 'Talent Acquisition' present and company's name present in either title or snippet
                                if link and 'talent acquisition' in title and company.lower() in (title + snippet):
                                    hr_name = result.get('title', '').split(' - ')[0].split(' at ')[0].strip()
                                    results.append({
                                        'Company': company,
                                        'HR Name': hr_name,
                                        'LinkedIn Profile': link
                                    })
                        
                        final_excel = save(results)
                        st.success("✅ All Profiles fetched successfully!")

                        st.download_button(
                                label="📥 Download HR Profiles Excel",
                                data=final_excel,
                                file_name="HR_Profiles.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            )

                    else :
                        st.info("Please upload at least one file to continue.")
    except Exception as e:
        st.info("Please upload file which has company as a column")

    
    
if __name__=="__main__":
    main()  


        
