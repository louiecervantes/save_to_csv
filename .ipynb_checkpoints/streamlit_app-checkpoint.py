#Input the relevant libraries
import streamlit as st
import altair as alt
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def chunker(input_data, N):
    input_words = input_data.split(' ')
    output = []
    cur_chunk = []
    count = 0
    for word in input_words:
        cur_chunk.append(word)
        count += 1
        if count == N:
            output.append(' '.join(cur_chunk))
            count, cur_chunk = 0, []
    output.append(' '.join(cur_chunk))
    return output

# Define the Streamlit app
def app():
    
    st.title('NLP Bag of Words')     
    st.subheader('(c) 2023 Louie F. Cervantes M. Eng.')
                 
    st.write('Extracting the frequency of terms using a Bag of Words model')
                 
    st.write("One of the main goals of text analysis is to convert text into numeric form so that we can use machine learning on it. Let's consider text documents that contain many millions of words. In order to analyze these documents, we need to extract the text and convert it into a form of numeric representation.")
    
    st.subheader('A large volume of text')
    st.write('input a reasonably long block of text about 300 words or longer. The provided example is the same one used in chinking.')
    
    # Create a long text block
    text_block = 'The Bill of Rights\nSECTION 1. No person shall be deprived of life, liberty, or property without due process of law, nor shall any person be denied the equal protection of the laws.\nSECTION 2. The right of the people to be secure in their persons, houses, papers, and effects against unreasonable searches and seizures of whatever nature and for any purpose shall be inviolable, and no search warrant or warrant of arrest shall issue except upon probable cause to be determined personally by the judge after examination under oath or affirmation of the complainant and the witnesses he may produce, and particularly describing the place to be searched and the persons or things to be seized.\nSECTION 3. (1) The privacy of communication and correspondence shall be inviolable except upon lawful order of the court, or when public safety or order requires otherwise as prescribed by law.\n(2) Any evidence obtained in violation of this or the preceding section shall be inadmissible for any purpose in any proceeding.\nSECTION 4. No law shall be passed abridging the freedom of speech, of expression, or of the press, or the right of the people peaceably to assemble and petition the government for redress of grievances.\nSECTION 5. No law shall be made respecting an establishment of religion, or prohibiting the free exercise thereof. The free exercise and enjoyment of religious profession and worship, without discrimination or preference, shall forever be allowed. No religious test shall be required for the exercise of civil or political rights.\nSECTION 6. The liberty of abode and of changing the same within the limits prescribed by law shall not be impaired except upon lawful order of the court. Neither shall the right to travel be impaired except in the interest of national security, public safety, or public health, as may be provided by law.\nSECTION 7. The right of the people to information on matters of public concern shall be recognized. Access to official records, and to documents, and papers pertaining to official acts, transactions, or decisions, as well as to government research data used as basis for policy development, shall be afforded the citizen, subject to such limitations as may be provided by law.\nSECTION 8. The right of the people, including those employed in the public and private sectors, to form unions, associations, or societies for purposes not contrary to law shall not be abridged.\nSECTION 9. Private property shall not be taken for public use without just compensation.\nSECTION 10. No law impairing the obligation of contracts shall be passed.\nSECTION 11. Free access to the courts and quasi-judicial bodies and adequate legal assistance shall not be denied to any person by reason of poverty.\nSECTION 12. (1) Any person under investigation for the commission of an offense shall have the right to be informed of his right to remain silent and to have competent and independent counsel preferably of his own choice. If the person cannot afford the services of counsel, he must be provided with one. These rights cannot be waived except in writing and in the presence of counsel.\n(2) No torture, force, violence, threat, intimidation, or any other means which vitiate the free will shall be used against him. Secret detention places, solitary, incommunicado, or other similar forms of detention are prohibited.\n(3) Any confession or admission obtained in violation of this or Section 17 hereof shall be inadmissible in evidence against him.\n(4) The law shall provide for penal and civil sanctions for violations of this section as well as compensation to and rehabilitation of victims of torture or similar practices, and their families.\nSECTION 13. All persons, except those charged with offenses punishable by reclusion perpetua when evidence of guilt is strong, shall, before conviction, be bailable by sufficient sureties, or be released on recognizance as may be provided by law. The right to bail shall not be impaired even when the privilege of the writ of habeas corpus is suspended. Excessive bail shall not be required.\nSECTION 14. (1) No person shall be held to answer for a criminal offense without due process of law.\n(2) In all criminal prosecutions, the accused shall be presumed innocent until the contrary is proved, and shall enjoy the right to be heard by himself and counsel, to be informed of the nature and cause of the accusation against him, to have a speedy, impartial, and public trial, to meet the witnesses face to face, and to have compulsory process to secure the attendance of witnesses and the production of evidence in his behalf. However, after arraignment, trial may proceed notwithstanding the absence of the accused provided that he has been duly notified and his failure to appear is unjustifiable.\nSECTION 15. The privilege of the writ of habeas corpus shall not be suspended except in cases of invasion or rebellion when the public safety requires it.\nSECTION 16. All persons shall have the right to a speedy disposition of their cases before all judicial, quasi-judicial, or administrative bodies.\nSECTION 17. No person shall be compelled to be a witness against himself.\nSECTION 18. (1) No person shall be detained solely by reason of his political beliefs and aspirations.\n(2) No involuntary servitude in any form shall exist except as a punishment for a crime whereof the party shall have been duly convicted.\nSECTION 19. (1) Excessive fines shall not be imposed, nor cruel, degrading or inhuman punishment inflicted. Neither shall death penalty be imposed, unless, for compelling reasons involving heinous crimes, the Congress hereafter provides for it. Any death penalty already imposed shall be reduced to reclusion perpetua.\n(2) The employment of physical, psychological, or degrading punishment against any prisoner or detainee or the use of substandard or inadequate penal facilities under subhuman conditions shall be dealt with by law.\nSECTION 20. No person shall be imprisoned for debt or non-payment of a poll tax.\nSECTION 21. No person shall be twice put in jeopardy of punishment for the same offense. If an act is punished by a law and an ordinance, conviction or acquittal under either shall constitute a bar to another prosecution for the same act.\nSECTION 22. No ex post facto law or bill of attainder shall be enacted.'

    user_input = st.text_area('Input the block of words here', text_block, height=290)
    from nltk.stem import wordnet
    from nltk.stem import WordNetLemmatizer

    with st.echo(code_location='below'):
        if st.button('Submit'):    
                   
            # Define the number of words in each chunk
            chunk_size = 600
            
            text_chunks = chunker(user_input, chunk_size)

            # Convert to dict items
            chunks = []
            for count, chunk in enumerate(text_chunks):
                d = {'index': count, 'text': chunk}
                chunks.append(d)

            # Extract the document term matrix
            count_vectorizer = CountVectorizer(min_df=2, max_df=30)
            document_term_matrix = count_vectorizer.fit_transform([chunk['text'] for chunk in chunks])
            
            # Extract the vocabulary and display it
            vocabulary = np.array(count_vectorizer.get_feature_names_out())
            
            
            # Generate names for chunks
            chunk_names = []
            for i in range(len(text_chunks)):
                chunk_names.append('Chunk-' + str(i+1))

            # Print the document term matrix
            st.text("\nDocument term matrix:")
                               
            output = []  
            output.append(['Word'] + [chunkname for chunkname in chunk_names])
            for word, item in zip(vocabulary, document_term_matrix.T):             
                # 'item' is a 'csr_matrix' data structure
                output.append([word] + [str(freq) for freq in item.data])

            df = pd.DataFrame(output)
            st.write(df)
            
             
# run the app
if __name__ == "__main__":
    app()
