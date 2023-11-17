import pytest
from sparse_recommender import SparseMatrix

def test_set_get_value():
    matrix = SparseMatrix(3, 3)
    matrix.set(0, 0, 11)
    assert matrix.get(0, 0) == 11

def test_recommend():
    matrix = SparseMatrix(3, 3)
    matrix.set(0, 0, 5)
    matrix.set(1, 2, 3)
    user_vector = [1, 2, 1]
    recommendations = matrix.recommend(user_vector)
    assert recommendations == [5, 3, 0]

def test_add_movie():
    matrix1 = SparseMatrix(2, 2)
    matrix1.set(0, 0, 1)
    matrix2 = SparseMatrix(2, 2)
    matrix2.set(0, 1, 2)
    result_matrix = matrix1.add_movie(matrix2)
    assert result_matrix.get(0, 0) == 1
    assert result_matrix.get(0, 1) == 2

def test_to_dense():
    matrix = SparseMatrix(2, 2)
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    dense_matrix = matrix.to_dense()
    assert dense_matrix == [[1, 0], [0, 2]]

def test_recommend_empty_user_vector():
    matrix = SparseMatrix(3, 3)
    matrix.set(0, 0, 5)
    matrix.set(1, 2, 3)
    user_vector = []  # Empty user vector
    with pytest.raises(ValueError):
        matrix.recommend(user_vector) 

def test_add_movie_negative_value():
    matrix1 = SparseMatrix(2, 2)
    matrix1.set(0, 0, 1)
    matrix2 = SparseMatrix(2, 2)
    matrix2.set(0, 1, -2)  # Attempt to add a matrix with a negative value
    with pytest.raises(ValueError):
        matrix1.add_movie(matrix2)  # Should raise an error

def test_to_dense_empty_matrix():
    matrix = SparseMatrix(3, 3)
    dense_matrix = matrix.to_dense()
    assert dense_matrix == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]