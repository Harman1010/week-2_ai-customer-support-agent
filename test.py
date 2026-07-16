from backend.service import get_answer

def main():

    print("Welcome to AI Customer Support!")

    print("\n")

    print("Write 'exit' to quit")

    while(True):

        query = input("Query").strip()

        if(query.lower() == "exit"):
            
            print("Thanks for your time!")

            break

        response = get_answer(query)

        print(f"Assistant : {response}")

if __name__ == "__main__" :

    main()
