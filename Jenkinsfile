pipeline {
    agent {
	label 'python'
	} 
    
    stages {
        stage('setup env') {
            steps {
                sh '''
		    pip install tox
		    pip install pytest
                    pip install -r requirements.txt
                    '''
            }
        }
        
        stage('tests proyect') {
            steps {
                sh '''
		   tox -e test_service
		   '''
            }
        }
        
        stage('Test_Code_Style') {
            steps {
                sh 'echo "Esto seria un modulo a integrar en el futuro"'
            }
        }
        
        stage('Security check') {
            steps {
                sh 'echo "Esto seria un modulo a integrar en el futuro"'
            }
        }
        
        stage('library generation') {
	    when {
		branch 'main'
	    }
            steps {
                sh '''python setup.py sdist'''
            }
        }
    }
}

