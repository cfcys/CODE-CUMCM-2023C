function [lambda1_max,lambda2_max,lambda3_max] = Experiment(X,L,A,C,P)
%EXPERIMENT �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
% lambda1 = 0;
% lambda2 = 0;
% lambda3 = 0;
Aver_max = 0;
lambda1_max = 0;
lambda2_max = 0;
lambda3_max = 0;

progressbar('1')
for lambda1 = 0.01:0.01:1
    for lambda2 = 0.01:0.01:1
        for lambda3 = 0.01:0.01:1
            sum = 0;    % ��ÿһ��ʵ���������Ӹ�������
            for epoches = 1:1:100      % ����һ����ʵ��
                %% ���в���������
%                 X = 0.15;    % �����ʵĳ�ʼֵ����
                beta = 0.1.*randn(7,1) + 0;        % ���ؿ���ģ�����۵����
%                 L = 0.0586;    % ��ʧ�ʵĳ�ʼ����
%                 A = [36.34131919,39.44311919,42.19331919,40.34911919,47.38371919,38.25151919,41.92971919];    % Ԥ�Ƶ��������
%                 C = [7.514217752,7.306281111,7.265334588,7.435038128,7.265160312,7.215534581,7.086171692];   % �������
%                 P = 0.536;    % ӯ�����ʵĳ�ʼ����
        %         %% ������Ҫȷ���Ĳ���
        %         lambda1 = 0.3;
        %         lambda2 = 0.3;
        %         lambda3 = 0.3;
                %%  �µĲ���
                Profit = 0;   % �ܹ�׬��Ǯ
                Left = 0;  % ʣ�������
                %% ģ����̵Ŀ�չ
                for i = 1:1:7
                %     disp(['��ǰ�ǵ�',num2str(i),'�죺']);
                    if beta(i) < 0   % ˵������������,���費��ʣ�����ý������̶ֳȣ�����
                        str ='����������';
                        % �Ƚ��н���
                        Sold = A(1) * (1 + beta(i));   % �Ѿ�����ȥ������
                        Get_Single = C(i) * P;
                        Profit = Profit + Sold * Get_Single;
                        Left = Left*L + A(i) * (X - beta(i) );     
                        % һ��Ľ��׽��� �����ݽ��и���
                        if i ~=7
                            P = P * (1 + lambda1 * beta(i));   % �۸��½�
                            X = X * (1 + lambda2 * beta(i));  %  �������½�
                            beta(i+1) = beta(i + 1 ) - lambda3 * beta(i);   % ���ڼ۸��½���Ⱥ�ڹ�����Ը������Ļ���������
                        end
                    elseif Left*L + A(i)*(1 + X) < A(i)*(1 +  beta(i))      % ʣ�µĺͻ�������½��Ķ������� Ҳ�����ϻ���
                        str ='��ϻ���';
                        % �Ƚ��н���
                        Sold = Left + A(i)*(1 + X);   % �Ѿ�����ȥ������
                        Get_Single = C(i) * P;
                        Profit = Profit + Sold * Get_Single;
                        Left = 0;     % Ҫ�ģ�����  
                        % һ��Ľ��׽��� �����ݽ��и���
                        if i ~=7
                            P = P * (1 + lambda1 * beta(i));   % �۸�����
                            X = X * (1 + lambda2 * beta(i));  %  ����������
                            beta(i+1) = beta(i + 1 ) - lambda3 * beta(i);   % ���ڼ۸�������Ⱥ�ڹ�����Ը������Ļ������½�
                        end
                    else     % ��Ԥ�����ã�����û�����ϻ������
                        str ='������Ԥ������';
                        Sold = A(1) * (1 + beta(i));   % �Ѿ�����ȥ������
                        Get_Single = C(i) * P;
                        Profit = Profit + Sold * Get_Single;
                        Left = Left*L + A(i) * (X - beta(i) );  
                        if i ~=7
                            P = P * (1 + lambda1 * beta(i));   % �۸�����
                            X = X * (1 + lambda2 * beta(i));  %  ����������
                            beta(i+1) = beta(i + 1 ) - lambda3 * beta(i);   % ���ڼ۸�������Ⱥ�ڹ�����Ը������Ļ������½�
                        end
                    end
                    % disp(['��',num2str(i),'��һ������',num2str(Sold),'����Ʒ,��������������',str]) 
                end
                % disp(['Ŀǰʣ��:',num2str(Left),'�ܵ�������:',num2str(Profit)])
                sum = sum + Profit;
            end
            aver = sum / epoches;
            % disp(['�ڲ���1=',num2str(lambda1),'�ڲ���2=',num2str(lambda2),'�ڲ���3=',num2str(lambda3),'�������,ӯ����ƽ��ֵΪ',num2str(aver)])
            if aver > Aver_max
                Aver_max = aver;
                lambda1_max = lambda1;
                lambda2_max = lambda2;
                lambda3_max = lambda3;
            end
            progressbar(lambda1/1)
        end
    end
%     progress_bar(lambda1, 0, 1);
end
disp(['�������������ڲ���1=',num2str(lambda1_max),'�ڲ���2=',num2str(lambda2_max),'�ڲ���3=',num2str(lambda3_max),'�������,�����ӯ����ƽ��ֵΪ',num2str(Aver_max)])

end

