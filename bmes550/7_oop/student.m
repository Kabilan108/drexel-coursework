clasdef student < person
    properties
        program;
        concentration;
        degreeyear;
        coursegrade;
    end

    methods
        function s=student(inname,inage,inzipcode,incoursegrade)
            s@person(inname,inage,inzipcode);
            s.coursegrade=incoursegrade;
        end

        function disp( p )
            % fprintf('Person: %s (%d) from zipcode:%d\n', p.name, p.age, p.zipcode);
            x = struct('name', p.name, 'age',p.age, 'program',p.program ...
            ,'concentration',p.concentration, 'degreeyear',p.degreeyear ...
            ,'coursegrade',p.coursegrade);
            disp(x);
        end

        function out=double(s)
            out=s.coursegrade;
        end

        function out= plus(a,b)
            out = a.coursegrade + b.coursegrade;
        end
    end

ends
