def test_ucsd_college():
    assert callable (ucsd_college)
    assert ucsd_college("6") in sixth_student_out
    assert ucsd_college("muir") in muir_student_out
    assert ucsd_college("erc") in erc_student_out
    assert "I don't think that's a college here on campus. Can you try typing your college again." is str
    
    
def test_ucsd_major():
    assert callable (ucsd_major)
    assert ucsd_major("international") in uncommon_out
    assert ucsd_major("idk") in undeclared_out
    assert anthropology_out is list 
    assert "I don't recognize that major. Can you try typing out your major again?" is str
  