import numpy as np
from collections import defaultdict


def cbow(corpus, window_size, embedding_size, learning_rate, epochs):
    # Create a vocabulary of unique words in the corpus
    vocab = list(set(corpus.split()))

    # Initialize word embeddings randomly
    embeddings = defaultdict(lambda: np.random.randn(embedding_size))

    # Train the embeddings using the CBOW algorithm
    for epoch in range(epochs):
        loss = 0
        for i in range(window_size, len(corpus) - window_size):
            # Extract the context words and the target word
            context_words = [
                corpus[j] for j in range(i - window_size, i + window_size + 1) if j != i
            ]
            target_word = corpus[i]

            # Compute the context embedding by averaging the embeddings of the context words
            context_embedding = np.mean([embeddings[w] for w in context_words], axis=0)

            # Compute the predicted embedding for the target word by taking the dot product with the context embedding
            predicted_embedding = np.dot(embeddings[target_word], context_embedding)

            # Compute the error between the predicted embedding and the actual embedding for the target word
            error = predicted_embedding - embeddings[target_word]

            # Update the embedding for the target word and the context words using the error and the learning rate
            embeddings[target_word] += learning_rate * error
            for w in context_words:
                embeddings[w] += learning_rate * error / (2 * window_size)

            # Accumulate the loss for this iteration
            loss += np.sum(error**2)

        # Print the loss for this epoch
        print("Epoch {}, loss: {:.2f}".format(epoch + 1, loss))

    # Return the trained embeddings
    return embeddings


corpus = "the quick brown fox jumped over the lazy dog"
embeddings = cbow(corpus, window_size=2, embedding_size=10, learning_rate=0.1, epochs=50)
print(embeddings["quick"])
